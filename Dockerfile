################
# Stage: Build #
################

FROM python:3.8.10-slim AS build

ENV POETRY_VERSION=1.6.1

WORKDIR .

# Export poetry dependencies to file
RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml ./
RUN python -m venv .venv
RUN poetry export --without-hashes --format requirements.txt --output ./requirements.txt

#####################
# Stage: Production #
#####################
FROM python:3.8.10-slim AS prod

ENV PYTHONPATH=.

WORKDIR .

# Copy requirements from build stage, and install them
COPY --from=build ./requirements.txt . 
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Run server
EXPOSE ${PORT:-8050}
CMD python src/app.py
