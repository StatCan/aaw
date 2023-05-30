for f in $(find . -name '*.py');
do
    docker run -v $(pwd)/:/tmp/ aaw-dev-docs:0.1.0 $f
    DIRNAME=$(dirname $f)
    FILENAME=$(basename $f)
    BASENAME="${FILENAME%.*}"
    mv $BASENAME.png $DIRNAME/$BASENAME.png
done