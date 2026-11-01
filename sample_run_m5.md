# Sample Run — Provenance Guard

One submission and one appeal, pasted as text. Requests, responses, and the
audit log entries afterwards.

## A submission

Request:

    $ curl -X POST http://127.0.0.1:5000/submit \
      -H "Content-Type: application/json" \
      -d '{"text":"The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must handle a wide variety of inputs.","creator_id":"sample_user"}'

Response:

    {
      "confidence": 0.7001,
      "content_id": "13350cb1-b6c0-4030-a9a2-32d7d871b202",
      "guess": "unsure",
      "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
      "model_score": 0.8309,
      "style_score": 0.5038
    }

Note: model_score and style_score are both in the response — Unit 8's
run_attacks.py and run_eval.py read them straight off here.

## An appeal

Request (using the content_id from the submission above):

    $ curl -X POST http://127.0.0.1:5000/appeal \
      -H "Content-Type: application/json" \
      -d '{"content_id":"8d9d15e5-2432-4f81-b626-3f51463d0c64","reasoning":"I wrote this myself. It is my own work."}'

Response:

    {
      "content_id": "8d9d15e5-2432-4f81-b626-3f51463d0c64",
      "message": "Your appeal has been recorded. A person will review it.",
      "ok": true,
      "status": "under_review"
    }

## What the log shows afterwards

    $ curl "http://127.0.0.1:5000/log?limit=6"

    {
      "count": 6,
      "entries": [
        {
          "combined_score": 0.675,
          "content_id": "519be8a4-7b3f-4c60-8f71-2f77510b1a93",
          "creator_id": "calib_human_formal",
          "guess": "unsure",
          "label": "PLACEHOLDER label (filled in at Milestone 5)",
          "model_score": 0.8216,
          "status": "decided",
          "style_score": 0.4551,
          "timestamp": "2026-11-01T07:47:56+00:00"
        },
        {
          "combined_score": 0.5964,
          "content_id": "9f492972-ae79-4ed4-a2c6-fb283ec8d007",
          "creator_id": "calib_edited_ai",
          "guess": "unsure",
          "label": "PLACEHOLDER label (filled in at Milestone 5)",
          "model_score": 0.7286,
          "status": "decided",
          "style_score": 0.398,
          "timestamp": "2026-11-01T07:47:57+00:00"
        },
        {
          "combined_score": 0.6262,
          "content_id": "09d34803-2c14-4137-a026-1d78b363ae57",
          "creator_id": "calib_ai",
          "guess": "unsure",
          "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
          "model_score": 0.7692,
          "status": "decided",
          "style_score": 0.4118,
          "timestamp": "2026-11-01T08:20:51+00:00"
        },
        {
          "combined_score": 0.5624,
          "content_id": "8d9d15e5-2432-4f81-b626-3f51463d0c64",
          "creator_id": "label_human_test",
          "guess": "unsure",
          "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
          "model_score": 0.8311,
          "status": "decided",
          "style_score": 0.1985,
          "timestamp": "2026-11-01T08:20:52+00:00"
        },
        {
          "combined_score": 0.5598,
          "content_id": "82820399-1067-4b8b-9595-91921c26bbc2",
          "creator_id": "calib_human_email",
          "guess": "unsure",
          "label": "We're not sure who wrote this. It could be either, so we're not making a call either way.",
          "model_score": 0.6133,
          "status": "decided",
          "style_score": 0.4796,
          "timestamp": "2026-11-01T08:20:53+00:00"
        },
        {
          "content_id": "8d9d15e5-2432-4f81-b626-3f51463d0c64",
          "creator_id": "label_human_test",
          "event": "appeal",
          "reasoning": "I wrote this myself. It is my own work.",
          "status": "under_review",
          "timestamp": "2026-11-01T08:27:29+00:00"
        }
      ]
    }

The original decision for 8d9d15e5-... is still there, and the appeal sits
after it with status "under_review". The log is append-only: the original was
not overwritten.