target_dir=s3
while read filename ; do
    part1=$(dirname "$filename")
    part2=$(basename "$filename")
    mkdir -p $target_dir/$part1
    # wget https://uk1s3.embassy.ebi.ac.uk/$filename -O s3-temp/$filename
    curl https://uk1s3.embassy.ebi.ac.uk/$filename -o $target_dir/$filename
done < example-model-files.txt