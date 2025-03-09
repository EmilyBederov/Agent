# 🍽️ CraveControl: AI-Powered Smart Meal Recommendation System 🤖

## What is CraveControl?
CraveControl is an **AI-driven interactive agent** designed to help users find **personalized, healthy meals** based on their cravings, dietary needs, and available ingredients. No more searching for recipes only to realize you're missing half the ingredients! 🚀

## How It Works
1. **User Input**  
   - The user provides details such as **height, weight, age, BMI, and caloric needs**.  
   - They also specify **cravings** (e.g., "I want something cheesy and spicy") and list **available ingredients** in their refrigerator.  

2. **Smart Meal Selection**   
   - CraveControl **calculates the optimal calorie intake** based on BMI and adjusts recommendations accordingly.  
   - It then searches for recipes that **match the user’s cravings** while ensuring they are **nutritionally balanced**.  
   - The system **filters recipes based on available ingredients**, ensuring the user can cook without needing extra grocery shopping.

3. **AI-Driven Recommendations** 🧠
   - Uses **embeddings and vector search** (Pinecone) to find the **most relevant recipes**.  
   - Retrieves recipes that are **healthy, satisfying, and convenient**.  
   - Leverages **LLMs to summarize and rank reviews**, ensuring the user gets **highly-rated** meal options.

## Why Use CraveControl?  
**Personalized Nutrition** – Meals are tailored to the user’s BMI and caloric needs.  
**Ingredient Matching** – No need to buy extra groceries; it works with what you have!  
**Craving Satisfaction** – AI finds the best match between what you want and what’s good for you.  
**Health-Conscious Choices** – Ensures meals are **nutritionally balanced** while still enjoyable.  
**Fast & Smart Retrieval** – Uses **state-of-the-art embeddings & AI-powered search** for **quick meal recommendations**.

---
## Project Structure: Five Key Notebooks 

This project consists of **five Jupyter notebooks**, each handling a critical step in the CraveControl pipeline:

1. **Recipe Pre-Processing Notebook**   
   - Cleans and structures the **raw recipe dataset**.  
   - Extracts key features (ingredients, categories, nutritional info).  
   - Prepares data for embedding generation.

2. **Recipe Embeddings & Pinecone Indexing Notebook**   
   - Generates **embeddings** for each recipe using an **LLM-powered embedding model**.  
   - Stores these embeddings in **Pinecone** for efficient similarity-based retrieval.

3. **Reviews Processing & Embedding Notebook** 
   - **Pre-processes user reviews**, cleaning and structuring them.  
   - Uses an **LLM to summarize** long reviews for better retrieval.  
   - Creates **embeddings** for the summarized reviews and **indexes them in Pinecone**.

4. **Ranking & LLM Chain Notebook** 
   - Contains the **Prompt Template** for interacting with the AI.  
   - **Calculates the top recipes** by matching user cravings, caloric needs, and available ingredients.  
   - Implements an **LLM-powered chain** to generate intelligent meal recommendations.

5. **User-Friendly Interface Notebook**  
   - The **final, ready-to-use notebook** for end users.  
   - Allows users to **input their cravings, available ingredients, and dietary needs**.  
   - Displays the **best recipe matches**, including **images and relevant details**.  

These notebooks work together to make CraveControl an **efficient and intelligent meal recommendation system**! 
---
## Data & File Overview (In `project_files.zip`)
This repository contains the dataset and embeddings powering CraveControl.

### 1. `env`
- Contains environment variables required for embedding generation and Pinecone usage.
- Includes:
  - `AZURE_OPENAI_API_KEY`: API key for Azure OpenAI.
  - `EMBEDDINGS_DEPLOYMENT`: Deployment name for embeddings.
  - `EMBEDDINGS_MODEL_NAME`: Model used for text embedding.
  - `AZURE_OPENAI_ENDPOINT`: API endpoint.
  - `EMBEDDINGS_API_VERSION`: API version.
  - `PINECONE_API_KEY`: API key for Pinecone.

### 2. `final_docs.json`
- Contains **20,000 recipes**.
- Each recipe is stored as a **LangChain document** with:
  - **Text of the recipe** (used as input for the embedding model).
  - **Metadata** (features of the recipe such as ingredients, category, etc.).

### 3. `final_doc_texts.json`
- A **list of raw text** from each recipe.
- Extracted directly from `final_docs.json`.

### 4. `embeddings_and_ids.json`
- Stores:
  - **Recipe IDs**.
  - **Corresponding embeddings** of **reviews** related to these recipes.

### 5. `embedding_data.json`
- A list of **text extracted from the reviews**.
- These reviews were used to generate embeddings.

### 6. `final_summary.json`
- Summarization of each review after being **processed through an LLM**.

### 7. `processed_reviews.json`
- Contains **pre-processed reviews** before summarization.
- This includes cleaning, filtering, and structuring the raw review data.

### 8. `selected_recipe_ids.json`
- Contains **the IDs of selected reviews** after preprocessing both:
  - Recipes.
  - Reviews.

### 9. `recipes_final.csv`
- A **compiled dataset** containing:
  - Recipes with corresponding reviews.
  - Additional recipes that were reviewed.
  - This dataset is the **final version** used for embeddings and retrieval.

## Usage
- The dataset can be used for **retrieval-augmented generation (RAG)** for recipe recommendations.
- Pinecone is used for **efficient similarity search** based on embeddings.
- The summarized reviews help in **ranking recipes** for user preferences.

---

This repository supports the **AI-driven meal recommendation system** by efficiently matching recipes with user preferences using embeddings. 🚀🍽️
