# imports
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from googleapiclient.discovery import build

# helper functions
def check_facts(text: str) -> int:
  api_url = f"https://toolbox.google.com/factcheck/api/v1/claimsearch?query={text[:200]}"
  try:
    response = requests.get(api_url)
    data = response.json()
    if "claims" in data and data["claims"]:
      return 80
    return 40
  except:
    return 50

def check_google_scholar(url: str) -> int:
  serpapi_key = "YOUR SerpAPI_Key HERE"
  params = {"q": url, "engine": "google_scholar", "api_key": serpapi_key}
  try:
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    return len(data.get("organic_results", []))
  except:
    return 0

# main function
# Step 1
def rate_url_validity(user_query: str, url: str) -> dict:
  try:
    response = requests.get(url, timeout = 10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    page_text = " ".join([p.text for p in soup.find_all("p")])
  except Exception as e:
    return {"error": f"Failed to fetch content: {str(e)}"}
# Step 2
  domain_trust = 60
# Step 3
  model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
  similarity_score = util.pytorch_cos_sim(model.encode(user_query), model.encode(page_text)).item() * 100
# Step 4
  fact_check_score = check_facts(page_text)
# Step 5
  sentiment_pipeline = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment")
  sentiment_result = sentiment_pipeline(page_text[:512])[0]
  bias_score = 100 if sentiment_result["label"] == "POSITIVE" else 50 if sentiment_result["label"] == "NEUTRAL" else 30
# Step 6
  citation_count = check_google_scholar(url)
  citation_score = min(citation_count * 10, 100)
# Step 7
  final_score = (
      (0.3 * domain_trust) +
      (0.3 * similarity_score) +
      (0.2 * fact_check_score) +
      (0.1 * bias_score) +
      (0.1 * citation_score)
  )

  return {
      "Domain Trust": domain_trust,
      "Content Relevance": similarity_score,
      "Fact-Check Score": fact_check_score,
      "Bias Score": bias_score,
      "Citation Score": citation_score,
      "Final Validity Score": final_score
  }

# test
user_prompt = "I have just been on an international flight, can I come back home to hold my 1-month-old newborn?"
url_to_check = "http://www.bhtp.com/blog/when-safe-to-travel-with-newborn/"
result = rate_url_validity(user_prompt, url_to_check)
print(result)