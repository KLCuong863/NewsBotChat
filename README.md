# NewsRAG-VN

Hệ thống Hỏi-Đáp tin tức tiếng Việt dựa trên Retrieval-Augmented Generation (RAG).

## 📁 Cấu trúc dự án

```text
NewsBotChat/
├── ingestion/          # Thu thập dữ liệu từ RSS và báo chí
├── indexing/           # Chunking, embedding và lập chỉ mục vào PostgreSQL/pgvector
├── retrieval/          # Tìm kiếm ngữ nghĩa (Semantic), BM25, Hybrid Search
├── generation/         # Tích hợp LLM sinh câu trả lời có trích dẫn nguồn
├── api/                # API phục vụ truy vấn (FastAPI)
├── eval/               # Đánh giá độ chính xác, faithfulness, ablation study
├── notebooks/          # Phân tích, thử nghiệm mô hình và trực quan hóa
├── docs/               # Tài liệu dự án, nhật ký học tập
├── docker-compose.yml  # Dịch vụ PostgreSQL + pgvector
├── requirements.txt    # Danh sách thư viện Python
└── .env                # Biến môi trường (không commit)
```

## 🚀 Bắt đầu nhanh

### 1. Kích hoạt môi trường ảo
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Cài đặt thư viện
```powershell
pip install -r requirements.txt
```

### 3. Kiểm tra nguồn tin tức
```powershell
python ingestion/check_sources.py
```

### 4. Kiểm tra mô hình Embedding
```powershell
python notebooks/smoke_test.py
```
