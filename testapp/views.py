from django.shortcuts import render

from .githubapi import search_repositories
from .models import Repository
#from .github_api import search_repositories

def home(request):
    return render(request, 'home.html')

def search(request):
    query = request.GET.get('q')
    if query:
        results = search_repositories(query)
        # Save results to the database
        for repo in results['items']:
            Repository.objects.update_or_create(
                github_id=repo['id'],
                defaults={
                    'name': repo['name'],
                    'owner': repo['owner']['login'],
                    'description': repo['description'],
                    'stars': repo['stargazers_count'],
                    'forks': repo['forks_count'],
                }
            )
    return render(request, 'search.html', {'results': results['items']})

def repo_list(request):
    repos = Repository.objects.all()
    return render(request, 'repo_list.html', {'repos': repos})
