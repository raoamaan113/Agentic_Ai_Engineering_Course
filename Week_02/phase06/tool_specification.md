
# Tool Specification: get_post_tool

## Tool Name
`get_post`

## Description
Retrieves a specific blog post by its unique ID from the JSONPlaceholder API. Useful when an agent needs to reference or display specific post content.

## HTTP Method
`GET`

## Endpoint
`https://jsonplaceholder.typicode.com/posts/{post_id}`

## Required Inputs
- `post_id` (integer): The unique identifier of the post to retrieve.

## Optional Inputs
- None

## Expected Output
A JSON object containing:
- `id` (int)
- `title` (string)
- `body` (string)
- `userId` (int)

## Possible Errors
- `404 Not Found`: Triggered if the `post_id` does not exist.
- `429 Too Many Requests`: Triggered if rate limits are exceeded.
- `Timeout`: Triggered if the server takes longer than the configured threshold.
- `500 Server Error`: Triggered if the remote server fails.

## Authentication Required
- None for this public endpoint (secured via bearer tokens on protected endpoints).