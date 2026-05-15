FROM ghcr.io/astral-sh/uv:alpine

ARG WORKDIR="/app/mpg-tracker"

ENV WORKDIR="$WORKDIR" \
    PYTHONPATH="$WORKDIR" \
    PATH="$PATH:$WORKDIR/.venv/bin"

COPY --chmod=444 pyproject.toml "$WORKDIR/"

WORKDIR "$WORKDIR"

RUN cd "$WORKDIR" && \
    uv sync && \
    uv cache clean

COPY --chmod=555 . "$WORKDIR"

CMD ["python", "api/main.py"]
