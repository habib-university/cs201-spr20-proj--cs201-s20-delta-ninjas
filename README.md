# CS201 - Data Structures 2 - Habib University, Karachi
## Team: Delta Ninjas
## Memebers: Anand Kumar, Ma'aaz A. Shaheen, Syed Safi, Saad Khan
Our project was to implemenet a data structure known as De Bruijn Graph and create one of its applications. De Bruijn Graphs 
are a special type of directed multi-graphs which help us solve assembly problems, such as the Shotest Common Superstring (SCS) Problem, 
in a very efficient way. 

We chose DNA Assembly as our application. Since, the DNA reads are too large and can't be read directly, we break them into
pieces, called the k-mers, and then create a De Bruijn Graph using these k-mers. Each node in the graph represents a (k-1)-mer. 
An Eulerian Walk over the De Bruijn graph will generate back the original DNA sequence.
### Terminology:
- k-mer: A short subsequence of length k contained within a sequence.
- (k-1)-mer: A subsequence of a k-mer with length k-1 (only 2 possible).
- Eulerian Walik: A walk through a graph that visits each edge exactly once.
### Requirements:
- Graphviz Library
- Graphviz windows application
### Poster Presentation Link: https://www.youtube.com/watch?v=2CTJPYUhnC4&feature=youtu.be
### Application Demonstration: https://www.youtube.com/watch?v=lltf4dOIt-E&feature=youtu.be
