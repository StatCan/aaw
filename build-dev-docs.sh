#!/usr/bin/env bash

# NOTE/WARNING: This will break once we go over 100 repos.
# Then we'll need to introduce pagination.


ORG=StatCan
DOCS_DIR=docs/dev/

camelcase () {
    echo $@ | tr '-' ' ' | sed 's/[^ ]\+/\L\u&/g'
}

let NUM_REPOS=$(curl --silent 'https://api.github.com/users/statcan' | jq -r .public_repos)

echo "Total number of repos: $NUM_REPOS"
echo "Fetching all READMEs. This might take a minute."
{
    let i=1
    while [ $NUM_REPOS -gt 0 ]; do
        let "NUM_REPOS-=50"
        echo curl --silent "https://api.github.com/users/StatCan/repos?per_page=50&page=$i" >&2
        curl --silent \
            -H 'Accept: application/vnd.github.mercy-preview+json' \
            "https://api.github.com/users/StatCan/repos?per_page=50&page=$i" |
            jq -cr '.[] | select(.topics | .[] | contains("daaas")) | @text "\(.name) \(.url) \(.html_url)"'
        ((i++))
    done
} |
    while IFS=" " read name url html_url; do
        NAME=$(camelcase $name)
        mkdir -p "$DOCS_DIR/$NAME/"
        for f in CHANGELOG.md README.md DEVELOPMENT.md; do
            # If the file exists, then write it to file and
            # prepend the filename.
            wget --quiet https://raw.githubusercontent.com/$ORG/$name/master/$f -O "$DOCS_DIR/$NAME/$f.tmp"
            if [ -s "$DOCS_DIR/$NAME/$f.tmp" ]; then
                cat <<EOF > "$DOCS_DIR/$NAME/$f"

$(cat "$DOCS_DIR/$NAME/$f.tmp")

# Link

[$name]($html_url)
EOF
            fi
            rm "$DOCS_DIR/$NAME/$f.tmp"
        done
done
