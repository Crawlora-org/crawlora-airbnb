use crawlora_airbnb::{AirbnbSearchParams, Client, ModelAirbnbSearchResponse};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .airbnb
        .search(AirbnbSearchParams {
            location: Some("Lisbon, Portugal".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelAirbnbSearchResponse = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
