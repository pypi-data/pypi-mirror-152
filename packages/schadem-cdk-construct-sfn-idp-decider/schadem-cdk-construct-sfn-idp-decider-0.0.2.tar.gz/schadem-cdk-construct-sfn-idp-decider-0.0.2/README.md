Construct as part of the IDP processing suite.

Takes a reference to an object on S3 and analyzes it and outputs a manifest definition for the IDP process.

# Input

```javascript
{
  "s3_bucket": "somebucket",
  "s3_key": "someprefix/someobject"
}
```

# Output

Manifest definition example

```javascript
{
  "manifest": {
    "S3Path": "s3://my-stack-dev-documentbucket04c71448-19ew04s4uhy8t/uploads"
  },
  "mime": "application/pdf",
  "classification": null,
  "numberOfPages": 12
}
```
