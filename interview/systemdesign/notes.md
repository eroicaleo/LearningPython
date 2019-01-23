# Lecture 1: Introducing system design & news feed system

## slide 1

* System Design/OO Design/API Design
* Need to check with HR, which kind of design will be in interview
* System design: high level
* OO/API Design: the interaction between classes.
* API Design questions: web technology
    * how dose mobile/web interaction
    * Given a class, define the interfaces and methods
    * Have to have project experiences, otherwise no feeling about why this design is good
      another design is bad
* The knowledge in this system design course is closely related to web technology.
    * web technology will always be needed
* System design: architecture/infrastructure
    * Covering database/website/mem-cache, how they work together to make a product
    * Today's topic news feed system: facebook/twitter/RSS

## slide 7

* System Design interview two forms:
    * Design Twitter/Facebook/Uber/Whatsapp/Yelp/Tiny URL/NoSQL
    * Trouble Shooting: what happened if we cannot access a website/webserver is too slow/for increasing traffic
* Couple years ago, how to design a whole system
* Nowadays, how to design a specific feature in the whole system

## slide 8

* Design a twitter/design a twitter feature

## slide 9

* Wrong solution #1: listing keyword: load balancer/MongoDB/...
* Veteran programmer, analyze what to do, step by step.
    * Start from a few users, maybe just 2. No need for anything fancy.
