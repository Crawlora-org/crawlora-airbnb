require "json"
require "net/http"
require "uri"

module Crawlora
  module Airbnb
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"airbnb-host": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-host", "method": "GET", "params": [{"description": "Host id (numeric)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "65056940"}], "path": "/airbnb/host/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "airbnb-host-listings": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-host-listings", "method": "GET", "params": [{"description": "Host id (numeric)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "65056940"}, {"description": "1-based page", "in": "query", "name": "page", "type": "integer"}], "path": "/airbnb/host/{id}/listings", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "airbnb-host-reviews": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-host-reviews", "method": "GET", "params": [{"description": "Host id (numeric)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "65056940"}, {"description": "1-based page", "in": "query", "name": "page", "type": "integer"}], "path": "/airbnb/host/{id}/reviews", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "airbnb-room": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-room", "method": "GET", "params": [{"description": "Room id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1384733959726184048"}], "path": "/airbnb/room/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "airbnb-room-calendar": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-room-calendar", "method": "GET", "params": [{"description": "Room id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1384733959726184048"}], "path": "/airbnb/room/{id}/calendar", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "airbnb-room-reviews": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-room-reviews", "method": "GET", "params": [{"description": "Room id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1384733959726184048"}, {"description": "1-based page", "in": "query", "name": "page", "type": "integer"}], "path": "/airbnb/room/{id}/reviews", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "airbnb-search": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-search", "method": "GET", "params": [{"description": "Location", "in": "query", "name": "location", "required": true, "type": "string", "x-example": "New York, NY"}, {"description": "Check-in date", "in": "query", "name": "check_in", "type": "string"}, {"description": "Check-out date", "in": "query", "name": "check_out", "type": "string"}, {"description": "Adult guests", "in": "query", "name": "adults", "type": "integer"}, {"description": "1-based page", "in": "query", "name": "page", "type": "integer"}, {"description": "Currency for bounded map search", "in": "query", "name": "currency", "type": "string"}, {"description": "Northeast latitude for bounded map search", "in": "query", "name": "ne_lat", "type": "number"}, {"description": "Northeast longitude for bounded map search", "in": "query", "name": "ne_lng", "type": "number"}, {"description": "Southwest latitude for bounded map search", "in": "query", "name": "sw_lat", "type": "number"}, {"description": "Southwest longitude for bounded map search", "in": "query", "name": "sw_lng", "type": "number"}, {"description": "Map zoom for bounded map search", "in": "query", "name": "zoom", "type": "integer"}], "path": "/airbnb/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "location", "required": true, "type": "string"}, {"in": "query", "name": "check_in", "type": "string"}, {"in": "query", "name": "check_out", "type": "string"}, {"in": "query", "name": "adults", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "currency", "type": "string"}, {"in": "query", "name": "ne_lat", "type": "number"}, {"in": "query", "name": "ne_lng", "type": "number"}, {"in": "query", "name": "sw_lat", "type": "number"}, {"in": "query", "name": "sw_lng", "type": "number"}, {"in": "query", "name": "zoom", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["airbnb-host", "airbnb-host-listings", "airbnb-host-reviews", "airbnb-room", "airbnb-room-calendar", "airbnb-room-reviews", "airbnb-search"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-airbnb-ruby/0.1.2", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('host') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('airbnb-host', params, response_type: response_type)
      end
      define_method('host_listings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('airbnb-host-listings', params, response_type: response_type)
      end
      define_method('host_reviews') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('airbnb-host-reviews', params, response_type: response_type)
      end
      define_method('room') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('airbnb-room', params, response_type: response_type)
      end
      define_method('room_calendar') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('airbnb-room-calendar', params, response_type: response_type)
      end
      define_method('room_reviews') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('airbnb-room-reviews', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('airbnb-search', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
