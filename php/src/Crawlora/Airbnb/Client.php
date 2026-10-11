<?php

declare(strict_types=1);

namespace Crawlora\Airbnb;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'airbnb';
    public const VERSION = '0.1.1';
    public const OPERATION_COUNT = 7;
    public const OPERATION_IDS = ["airbnb-host", "airbnb-host-listings", "airbnb-host-reviews", "airbnb-room", "airbnb-room-calendar", "airbnb-room-reviews", "airbnb-search"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"airbnb-host": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-host", "method": "GET", "params": [{"description": "Host id (numeric)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "65056940"}], "path": "/airbnb/host/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "airbnb-host-listings": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-host-listings", "method": "GET", "params": [{"description": "Host id (numeric)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "65056940"}, {"description": "1-based page", "in": "query", "name": "page", "type": "integer"}], "path": "/airbnb/host/{id}/listings", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "airbnb-host-reviews": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-host-reviews", "method": "GET", "params": [{"description": "Host id (numeric)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "65056940"}, {"description": "1-based page", "in": "query", "name": "page", "type": "integer"}], "path": "/airbnb/host/{id}/reviews", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "airbnb-room": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-room", "method": "GET", "params": [{"description": "Room id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1384733959726184048"}], "path": "/airbnb/room/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "airbnb-room-calendar": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-room-calendar", "method": "GET", "params": [{"description": "Room id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1384733959726184048"}], "path": "/airbnb/room/{id}/calendar", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "airbnb-room-reviews": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-room-reviews", "method": "GET", "params": [{"description": "Room id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1384733959726184048"}, {"description": "1-based page", "in": "query", "name": "page", "type": "integer"}], "path": "/airbnb/room/{id}/reviews", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "airbnb-search": {"bodyParam": null, "bodyRequired": false, "id": "airbnb-search", "method": "GET", "params": [{"description": "Location", "in": "query", "name": "location", "required": true, "type": "string", "x-example": "New York, NY"}, {"description": "Check-in date", "in": "query", "name": "check_in", "type": "string"}, {"description": "Check-out date", "in": "query", "name": "check_out", "type": "string"}, {"description": "Adult guests", "in": "query", "name": "adults", "type": "integer"}, {"description": "1-based page", "in": "query", "name": "page", "type": "integer"}, {"description": "Currency for bounded map search", "in": "query", "name": "currency", "type": "string"}, {"description": "Northeast latitude for bounded map search", "in": "query", "name": "ne_lat", "type": "number"}, {"description": "Northeast longitude for bounded map search", "in": "query", "name": "ne_lng", "type": "number"}, {"description": "Southwest latitude for bounded map search", "in": "query", "name": "sw_lat", "type": "number"}, {"description": "Southwest longitude for bounded map search", "in": "query", "name": "sw_lng", "type": "number"}, {"description": "Map zoom for bounded map search", "in": "query", "name": "zoom", "type": "integer"}], "path": "/airbnb/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "location", "required": true, "type": "string"}, {"in": "query", "name": "check_in", "type": "string"}, {"in": "query", "name": "check_out", "type": "string"}, {"in": "query", "name": "adults", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "currency", "type": "string"}, {"in": "query", "name": "ne_lat", "type": "number"}, {"in": "query", "name": "ne_lng", "type": "number"}, {"in": "query", "name": "sw_lat", "type": "number"}, {"in": "query", "name": "sw_lng", "type": "number"}, {"in": "query", "name": "zoom", "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-airbnb-php/0.1.1',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function host(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("airbnb-host", $params, $responseType);
    }
    public function host_listings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("airbnb-host-listings", $params, $responseType);
    }
    public function host_reviews(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("airbnb-host-reviews", $params, $responseType);
    }
    public function room(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("airbnb-room", $params, $responseType);
    }
    public function room_calendar(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("airbnb-room-calendar", $params, $responseType);
    }
    public function room_reviews(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("airbnb-room-reviews", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("airbnb-search", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
