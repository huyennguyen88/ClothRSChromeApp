import pandas as pd
import numpy as np
import pickle


global DOT
global COSINE



DOT = 'dot'
COSINE = 'cosine'

def _load_model_data():
    products = pd.read_pickle('data4server/products.pkl')
    file = open("data4server/embeddings.pkl", 'rb')
    embeddings = pickle.load(file)
    file.close()
    return products, embeddings


def _compute_similarity(query_embedding, item_embeddings, measure=DOT):
    """Tính điểm số giữa câu query và item embedding.
    Args:
      query_embedding: là một vector nhúng của query kích thước [k].
      item_embeddings: là ma trận nhúng véc tơ các items kích thước [N, k].
      measure: là một chuỗi string xác định kiểu đo lường tương đương được sử dụng. Có thể là theo phương pháp 'dot similarity' hoặc 'cosine similarity'.
    Returns:
      scores: một véc tơ kích thước [N], sao cho score[i] là điểm của item i được cho bởi query.
    """
    u = query_embedding
    V = item_embeddings
    if measure == COSINE:
        V = V / np.linalg.norm(V, axis=1, keepdims=True)
        u = u / np.linalg.norm(u)
    scores = u.dot(V.T)
    return scores


def _product_similarity(products, embeddings, product_id, measure=DOT, k=10):
    scores = _compute_similarity(
        embeddings["product_id"][product_id], embeddings["product_id"],
        measure)
    score_key = measure + ' score'
    df = pd.DataFrame({
        score_key: list(scores),
        'product_id': products['product_id']
    })
    df = df.sort_values([score_key], ascending=False).head(k)
    return  df['product_id'].values
