# scriptsMSR

Python modules for mining software repositories at GitHub.

## Usage

(a) Create a list of "popular" projects for a given programming language. 

    $ python list_projects.py
    Language (java, cpp, python,...): java
    Min. number of stars: 200
    Number of projects: 10
    Output file: java.projects

This creates a CSV file (named java.projects) with the 10 most popular Java projects (these projects must have at least 200 stars). The 
CSV file has a structure like this:

    # project_name ,   size, watchers, forks,                                   repo_url, description 
      elasticsearch, 235514,    14299,  4768, git://github.com/elastic/elasticsearch.git, Open Source, Distributed, RESTful Search Engine

(b) Clone the repositories from a list of GitHub projects specified as a CSV file with the structure discussed above
