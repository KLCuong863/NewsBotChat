from sentence_transformers import SentenceTransformer

# Tải model bge-m3 và chạy thử embedding
print("Loading model BAAI/bge-m3...")
m = SentenceTransformer("BAAI/bge-m3")
v = m.encode(["Giá xăng hôm nay tăng"], normalize_embeddings=True)
print("Embedding shape:", v.shape)
print("Smoke test thành công!")
