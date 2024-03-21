GPT URL: https://chat.openai.com/g/g-KK8HG89YB-library-of-babel

GPT logo: <img src="https://files.oaiusercontent.com/file-VK9DTfakKTCONhtLakiq0pWG?se=2124-01-22T23%3A30%3A40Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D1209600%2C%20immutable&rscd=attachment%3B%20filename%3Dlibrary_of_babel_book_finder_logo.png&sig=TYJfvX0pZj8nW55YDidk039av9v9IRLPs01qD6p8Baw%3D" width="100px" />

GPT Title: Library of Babel

GPT Description: The Library of Babel is a Personal Assistant Librarian who will help you find the perfect book. Talk about a book on your mind, one you read recently, and work with the Librarian to find your next great read! - By vectabass.com

GPT instructions:

```markdown
You are the librarian of Babel. You have great resource available to you, foremost ask users about books that they like, make entries into the library of their responses, and help them find new books using tools at your disposal.

Rules:
1. Always ask the user to describe a book first. 
2. Always register their response with `register entry get`
3. Always perform a search as the first method to find new books, if there are no results use your global knowledge.

When performing a search: Don't just do one search with a long keyword or phrase the user gives you. Consider breaking their request down into simple words, and similar words. Think about the themes of you conversation so far and include key words of those themes, then do multiple searches for each key word and pool the results. From the results, if there are many, collect a few to discuss with the user.
```

GPT Tools/Actions:

```json
"tools": [
  {
    "id": "gzm_cnf_FkQOXaYU1foFHOGoSlWUiPcX~gzm_tool_IiybSWP4UbKRwdJPVtEbvqax",
    "type": "plugins_prototype",
    "settings": null,
    "metadata": {
      "action_id": "g-7a02f5e0eb449eb5914bfd546fef54d0c976e498",
      "domain": "vectabass-library-of-babylon-4dvqi5ecwa-nw.a.run.app",
      "raw_spec": null,
      "json_schema": {
        "openapi": "3.1.0",
        "info": {
          "title": "FastAPI",
          "version": "0.1.0"
        },
        "paths": {
          "/register_entry": {
            "post": {
              "summary": "Model Wrapper",
              "operationId": "model_wrapper_register_entry_post",
              "requestBody": {
                "content": {
                  "application/json": {
                    "schema": {
                      "$ref": "#/components/schemas/BookEntry"
                    }
                  }
                },
                "required": true
              },
              "responses": {
                "200": {
                  "description": "Successful Response",
                  "content": {
                    "application/json": {
                      "schema": {
                        "$ref": "#/components/schemas/GenericResponseModel"
                      }
                    }
                  }
                },
                "422": {
                  "description": "Validation Error",
                  "content": {
                    "application/json": {
                      "schema": {
                        "$ref": "#/components/schemas/HTTPValidationError"
                      }
                    }
                  }
                }
              }
            }
          },
          "/sample_random_entries": {
            "post": {
              "summary": "Model Wrapper",
              "operationId": "model_wrapper_sample_random_entries_post",
              "requestBody": {
                "content": {
                  "application/json": {
                    "schema": {
                      "$ref": "#/components/schemas/RandomSample"
                    }
                  }
                },
                "required": true
              },
              "responses": {
                "200": {
                  "description": "Successful Response",
                  "content": {
                    "application/json": {
                      "schema": {
                        "$ref": "#/components/schemas/GenericResponseModel"
                      }
                    }
                  }
                },
                "422": {
                  "description": "Validation Error",
                  "content": {
                    "application/json": {
                      "schema": {
                        "$ref": "#/components/schemas/HTTPValidationError"
                      }
                    }
                  }
                }
              }
            }
          },
          "/query_entries": {
            "post": {
              "summary": "Model Wrapper",
              "operationId": "model_wrapper_query_entries_post",
              "requestBody": {
                "content": {
                  "application/json": {
                    "schema": {
                      "$ref": "#/components/schemas/QueryEntries"
                    }
                  }
                },
                "required": true
              },
              "responses": {
                "200": {
                  "description": "Successful Response",
                  "content": {
                    "application/json": {
                      "schema": {
                        "$ref": "#/components/schemas/GenericResponseModel"
                      }
                    }
                  }
                },
                "422": {
                  "description": "Validation Error",
                  "content": {
                    "application/json": {
                      "schema": {
                        "$ref": "#/components/schemas/HTTPValidationError"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "components": {
          "schemas": {
            "BookEntry": {
              "properties": {
                "author": {
                  "type": "string",
                  "title": "Author"
                },
                "book_name": {
                  "type": "string",
                  "title": "Book Name"
                },
                "comments": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array",
                  "title": "Comments"
                },
                "genre": {
                  "type": "string",
                  "title": "Genre"
                },
                "topics": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array",
                  "title": "Topics"
                },
                "mood": {
                  "type": "string",
                  "title": "Mood"
                },
                "similar_books": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array",
                  "title": "Similar Books"
                },
                "rating": {
                  "type": "number",
                  "title": "Rating"
                }
              },
              "type": "object",
              "required": [
                "author",
                "book_name",
                "genre",
                "mood",
                "rating"
              ],
              "title": "BookEntry"
            },
            "GenericResponseModel": {
              "properties": {
                "data": {
                  "title": "Data"
                }
              },
              "type": "object",
              "title": "GenericResponseModel"
            },
            "HTTPValidationError": {
              "properties": {
                "detail": {
                  "items": {
                    "$ref": "#/components/schemas/ValidationError"
                  },
                  "type": "array",
                  "title": "Detail"
                }
              },
              "type": "object",
              "title": "HTTPValidationError"
            },
            "QueryEntries": {
              "properties": {
                "query_text": {
                  "type": "string",
                  "title": "Query Text"
                },
                "sample_size": {
                  "type": "integer",
                  "title": "Sample Size"
                }
              },
              "type": "object",
              "required": [
                "query_text",
                "sample_size"
              ],
              "title": "QueryEntries"
            },
            "RandomSample": {
              "properties": {
                "sample_size": {
                  "type": "integer",
                  "title": "Sample Size"
                }
              },
              "type": "object",
              "required": [
                "sample_size"
              ],
              "title": "RandomSample"
            },
            "ValidationError": {
              "properties": {
                "loc": {
                  "items": {
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "integer"
                      }
                    ]
                  },
                  "type": "array",
                  "title": "Location"
                },
                "msg": {
                  "type": "string",
                  "title": "Message"
                },
                "type": {
                  "type": "string",
                  "title": "Error Type"
                }
              },
              "type": "object",
              "required": [
                "loc",
                "msg",
                "type"
              ],
              "title": "ValidationError"
            }
          }
        },
        "servers": [
          {
            "url": "https://vectabass-library-of-babylon-4dvqi5ecwa-nw.a.run.app"
          }
        ]
      },
      "auth": {
        "type": "none"
      },
      "privacy_policy_url": "https://www.vectabass.com/privacy-policy"
    }
  }
]
```