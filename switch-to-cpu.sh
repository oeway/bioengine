# Change to GPU to CPU
find ./s3/model-repository -type f -print0 | xargs -0 perl -pi -e 's/KIND_GPU/KIND_CPU/g'