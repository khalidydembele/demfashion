from django.shortcuts import render, get_object_or_404
from .models import Product, Highlight
from django.db.models import Q  # Import indispensable pour la recherche

def home(request):
    # Récupère les 3 dernières vidéos virales pour l'accueil
    highlights = Highlight.objects.all().order_by('-id')[:3]
    return render(request, 'index.html', {'highlights': highlights})

def boutique(request):
    query = request.GET.get('q')  # Récupère le texte de la barre de recherche
    if query:
        # Filtre les produits si une recherche est effectuée
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        # Sinon, affiche tous les produits
        products = Product.objects.all()
    
    return render(request, 'boutique.html', {'products': products})

def detail(request, pk):
    # Affiche la page de détail d'un produit spécifique
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'product': product})