GPT URL: https://chatgpt.com/g/g-470NtUZER-pip-install

GPT logo: <img src="https://files.oaiusercontent.com/file-9bJjpiY1IhBcm8SPREKj5mdw?se=2124-06-26T17%3A54%3A23Z&sp=r&sv=2023-11-03&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D-RIWgodF_400x400.jpg&sig=UjEjcEexg2tx3hncc%2B0aMX8ehDl2S7yxqY3dqVj8YEw%3D" width="100px" />

GPT Title: pip install

GPT Description: Allows download of python packages - By Nico Ritschel

GPT instructions:

```markdown
Allows for installation of python packages via a proxy. First list the versions for a given package (assume latest if they don't specify). Always select the version of the package you can install and then fetch that and install it. Only install packages via the action and then via the local file, since your interpreter can't talk to the internet.

The packages will be returned in parts. If just one part that's fine, you'll still need to "combine". Silently handle combination of the parts if need be before installing; you prefer installing .whl, so make sure you have a .whl.
```

GPT actions:

```json
"tools": [
  {
    "id": "Q8RCAWrGCH85mo5rJnzqla0c",
    "type": "plugins_prototype",
    "settings": null,
    "metadata": {
      "action_id": "g-0396e11690d066ca71aa0999ac9e076294956c50",
      "domain": "nicosuave-amberbat.web.val.run",
      "raw_spec": null,
      "json_schema": {
        "openapi": "3.1.0",
        "info": {
          "title": "PyPI Wheel API",
          "version": "1.0.0",
          "description": "API for listing and downloading wheel files from PyPI"
        },
        "servers": [
          {
            "url": "https://nicosuave-amberbat.web.val.run",
            "description": "Production server"
          }
        ],
        "paths": {
          "/api/wheels/{package}": {
            "get": {
              "operationId": "listWheels",
              "summary": "List wheels for a package",
              "description": "Retrieves a list of available wheel files for the specified package from PyPI.",
              "parameters": [
                {
                  "name": "package",
                  "in": "path",
                  "required": true,
                  "schema": {
                    "type": "string"
                  },
                  "description": "The name of the PyPI package"
                }
              ],
              "responses": {
                "200": {
                  "description": "Successful response",
                  "content": {
                    "application/json": {
                      "schema": {
                        "type": "object",
                        "properties": {
                          "wheels": {
                            "type": "array",
                            "items": {
                              "$ref": "#/components/schemas/WheelInfo"
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "400": {
                  "description": "Bad request",
                  "content": {
                    "text/plain": {
                      "schema": {
                        "type": "string"
                      }
                    }
                  }
                },
                "500": {
                  "description": "Internal server error",
                  "content": {
                    "text/plain": {
                      "schema": {
                        "type": "string"
                      }
                    }
                  }
                }
              }
            }
          },
          "/api/wheel/{package}/{filename}": {
            "get": {
              "operationId": "downloadWheel",
              "summary": "Download a wheel file",
              "description": "Downloads the specified wheel file for the given package from PyPI and returns it as base64-encoded data. If the file is larger than 9.5MB, it will be split into multiple parts.",
              "parameters": [
                {
                  "name": "package",
                  "in": "path",
                  "required": true,
                  "schema": {
                    "type": "string"
                  },
                  "description": "The name of the PyPI package"
                },
                {
                  "name": "filename",
                  "in": "path",
                  "required": true,
                  "schema": {
                    "type": "string"
                  },
                  "description": "The filename of the wheel to download"
                }
              ],
              "responses": {
                "200": {
                  "description": "Successful response",
                  "content": {
                    "application/json": {
                      "schema": {
                        "type": "object",
                        "properties": {
                          "openaiFileResponse": {
                            "type": "array",
                            "items": {
                              "$ref": "#/components/schemas/FileResponse"
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "400": {
                  "description": "Bad request",
                  "content": {
                    "text/plain": {
                      "schema": {
                        "type": "string"
                      }
                    }
                  }
                },
                "404": {
                  "description": "Wheel file not found",
                  "content": {
                    "text/plain": {
                      "schema": {
                        "type": "string"
                      }
                    }
                  }
                },
                "500": {
                  "description": "Internal server error",
                  "content": {
                    "text/plain": {
                      "schema": {
                        "type": "string"
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
            "WheelInfo": {
              "type": "object",
              "properties": {
                "filename": {
                  "type": "string",
                  "description": "The filename of the wheel file"
                },
                "url": {
                  "type": "string",
                  "format": "uri",
                  "description": "The download URL for the wheel file"
                },
                "size": {
                  "type": "integer",
                  "description": "The size of the wheel file in bytes"
                },
                "upload_time": {
                  "type": "string",
                  "format": "date-time",
                  "description": "The upload time of the wheel file"
                }
              },
              "required": [
                "filename",
                "url",
                "size",
                "upload_time"
              ]
            },
            "FileResponse": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "The name of the file part (e.g., filename.whl.part1)"
                },
                "mime_type": {
                  "type": "string",
                  "description": "The MIME type of the file"
                },
                "content": {
                  "type": "string",
                  "format": "byte",
                  "description": "The base64-encoded content of the file part"
                }
              },
              "required": [
                "name",
                "mime_type",
                "content"
              ]
            }
          }
        }
      },
      "auth": {
        "type": "none"
      },
      "privacy_policy_url": "https://nicosuave-crimsonmuskox.web.val.run"
    }
  }
],
```