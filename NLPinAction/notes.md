# Ch01

### 1.4.4 Another way

* Distance metrics are useful for spelling correctors and recognizing proper nouns.
* We use vector representations of natural language words and some distant metrics for
  those vectors.
* We can use `collections.Counter` to do frequency counter and it's good enough for
  email spam filter

## 1.5 A brief overflight of hyperspace

* We ask questions like that:
    * How likely is this message to be a question?
    * How much is it about a person / is it about me?
    * How angry or happen does it sound?
    * Is it something I need to respond to?
* Bit vector language model.
* Ch4 latent semantic indexing and latent Dirichlet allocation

## 1.6 Word order and grammer

* Previous sentence just ignored word order.
  For short sentence, it's OK if we just want to get general sense and sentiment.
* More complex statements can lost most their meaning when throw into a bag.
  A bag of words isn't the best way for processing DB query.

## 1.7 A chatbot natural language pipeline

* Parse: Extract feature
* Analyze: Generate and combine features
* Generate: Compose possible response
* Execute: 

### 1.8 Processing in depth

* Characters -> Tokens -> Tagged tokens -> Syntax Tree -> Entity relationship -> Knowledge base
* It's possible to build a useful and interesting chatbot using only a single layer of processing.
    * Like `ChatterBot` project, just compute the Levenshtein distance
    * `Will` labor intensive and data-light, good for Siri/Google now, and actually used in Slack

### 1.9 Natural language IQ

* Breadth and Depth
    * Alexa and Allo, more breadth
    * Google translate, more depth: feature extractors / decision trees and knowledge graphs are
      programmed
