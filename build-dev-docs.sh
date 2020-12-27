#!/usr/bin/env bash

# NOTE/WARNING: This will break once we go over 100 repos.
# Then we'll need to introduce pagination.


ORG=StatCan
DOCS_DIR=docs/dev/

camelcase () {
    echo $@ | tr '-' ' ' | sed 's/[^ ]\+/\L\u&/g'
}


# Repo blacklist
ignore () {
    cat <<EOF | grep -q "$1"
block-sequence
cae-eac
ccei
census_age65_vs_population_growth
census_birthplace
census_income
census_occupations
dataviz-components
dns
EpiSim
ESM-Mobile-App
experimental-react-native-app
experimental_data_api
express-api-server
jsonapi-pagination
jstree
katacoda-courses
MetaTagGenerator
orbital-viz
pg-evolve
site-ccei
time-series-library
transportation
website
wellBeingCheck
WellbeingCheckChangeRequest
WellbeingCheckUAT
wellbeing_react_native
EOF
}


let NUM_REPOS=$(curl --silent 'https://api.github.com/users/statcan' | jq -r .public_repos)

echo "Total number of repos: $NUM_REPOS"
echo "Fetching all READMEs. This might take a minute."
{
    let i=1
    while [ $NUM_REPOS -gt 0 ]; do
        let "NUM_REPOS-=50"
        echo curl --silent "https://api.github.com/users/statcan/repos?per_page=50&page=$i" >&2
        curl --silent "https://api.github.com/users/statcan/repos?per_page=50&page=$i"
        ((i++))
    done
} | jq -cr '.[] | @text "\(.name) \(.url)"' |
    while IFS=" " read name url; do
        # Keep a blacklist of repos
        ignore $name && continue

        NAME=$(camelcase $name)
        mkdir -p "$DOCS_DIR/$NAME/"
        for f in CHANGELOG.md README.md DEVELOPMENT.md; do
            # If the file exists, then write it to file and
            # prepend the filename.
            wget --quiet https://raw.githubusercontent.com/$ORG/$name/master/$f -O "$DOCS_DIR/$NAME/$f.tmp"
            if [ -s "$DOCS_DIR/$NAME/$f.tmp" ]; then
                cat <<EOF > "$DOCS_DIR/$NAME/$f"
Link: [$name]($url)

$(cat "$DOCS_DIR/$NAME/$f.tmp")
EOF
            fi
            rm "$DOCS_DIR/$NAME/$f.tmp"
        done
done
