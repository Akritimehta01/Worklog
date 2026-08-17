# API Testing Experiment

## Objective

To expose the text classification pipeline through a REST API and test its behavior with different inputs.

## API

**POST `/predict`**

The endpoint accepts text and returns its predicted sentiment.

### Positive Input

```json
{
  "text": "This application is excellent and helpful"
}