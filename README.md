# 🎬 Movie Recommendation System  

A machine learning project built in **Jupyter Notebook** that recommends movies to users based on their preferences.  

---

## 🚀 Project Overview  
This project focuses on building a **content-based recommendation system** that suggests movies similar to a given movie title. It uses movie metadata (title, genres, etc.) and computes similarity scores to recommend the top movies that are most relevant.  

---

## 🛠️ Tech Stack  
- **Python**  
- **Pandas** – Data manipulation  
- **NumPy** – Numerical operations  
- **Scikit-learn** – Text vectorization & similarity calculation  
- **Jupyter Notebook** – Development environment  

---

## 🧠 Approach  
1. **Data Loading & Cleaning**  
   - Loaded movie dataset (titles, genres, etc.).  
   - Handled missing values and preprocessed text.  

2. **Feature Engineering**  
   - Combined relevant features (like genres, overview).  
   - Converted text data into numerical representation using **TF-IDF / Count Vectorizer**.  

3. **Similarity Calculation**  
   - Computed **cosine similarity** between movie vectors.  

4. **Recommendation**  
   - For a given movie title, returned top N most similar movies.  

---

## 📸 Sample Output  
```text
Input Movie: Inception  
Recommended Movies:  
1. Interstellar  
2. The Matrix  
3. Shutter Island  
4. The Prestige  
5. Memento  
