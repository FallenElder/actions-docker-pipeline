FROM python:3.13-slim as builder
WORKDIR /home/api_python/

COPY ./python_api/requirements.txt ./
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.13-slim

WORKDIR /home/api_python/

RUN useradd api

COPY --from=builder /opt/venv /opt/venv
COPY ./python_api/rotas.py ./
COPY ./python_api/bd_com.py ./
COPY ./python_api/.env ./

ENV PATH="/opt/venv/bin:$PATH"

USER api

EXPOSE 3080

CMD ["uvicorn", "rotas:app", "--host", "0.0.0.0", "--port", "3080"]