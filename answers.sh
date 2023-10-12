#!/bin/bash
set -x

curl --location --request POST "https://searchassist.kore.ai/searchassistapi/public/searchAssist/stream/${APP_ID}/${SEARCH_ID}/fullSearch" \
--header "auth: ${SEARCH_ASSIST_JWT_TOKEN}" \
--header 'Content-Type: application/json' \
--data-raw "{ \"query\": \"${1}\", \"maxNumOfResults\":4 }"   | jq .template.graph_answer


