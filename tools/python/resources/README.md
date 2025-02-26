# Resources

Comando di esempio per estrarre i documenti JSON da ElasticSearch
```
curl -H 'Content-Type: application/json' localhost:9200/dasmemo2/_search?pretty -d '{"query":{"term":{"documentId":"7caba5736b1d9e26c1a5a8af278a3383"}}}' > 7caba5736b1d9e26c1a5a8af278a3383.json
```

