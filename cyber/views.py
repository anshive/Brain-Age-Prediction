from django.shortcuts import render
from django.contrib import messages
from user.models import Usermodel

import os
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error

def index(request):
    return render(request, "index.html")

def Home(request):
    return index(request)

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginaction(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['upasswd']
        if uname == 'admin' and passwd == 'admin':
            data = Usermodel.objects.all()
            return render(request, "admin/adminhome.html", {'data': data})
        else:
            messages.success(request, 'Incorrect Details')
            return render(request, "admin/adminlogin.html")
    return render(request, "admin/adminlogin.html")

def showusers(request):
    data = Usermodel.objects.all()
    return render(request, "admin/adminhome.html", {'data': data})

def AdminActiveUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        Usermodel.objects.filter(id=id).update(status=status)
        data = Usermodel.objects.all()
        return render(request, "admin/adminhome.html", {'data': data})

def logout(request):
    return render(request, "admin/adminlogin.html")

def ML(request):
    df = pd.read_csv(os.path.join(BASE_DIR, "media/brainage.csv"))

    # Create scatter plot
    plt.scatter(df['T1_chronAge'], df['T1_BrainAge'])
    plt.xlabel("ChronAge")
    plt.ylabel("BrainAge")
    plt.savefig(os.path.join(BASE_DIR, "media/scatter_plot.png"))
    plt.show()

    # Create bar plot
    plt.bar(df['T1_chronAge'], df['T1_BrainAge'])
    plt.xlabel("ChronAge")
    plt.ylabel("BrainAge")
    plt.savefig(os.path.join(BASE_DIR, "media/bar_plot.png"))
    plt.show()

    # Create line plot
    plt.plot(df['T1_chronAge'], df['T1_BrainAge'])
    plt.xlabel("ChronAge")
    plt.ylabel("BrainAge")
    plt.savefig(os.path.join(BASE_DIR, "media/line_plot.png"))
    plt.show()

    # Create pair plots
    sns.pairplot(df[['T1_BrainAge', 'T1_chronAge', 'T1_PAD', 'Age_at_onset', 'premorbidIQ']])
    plt.savefig(os.path.join(BASE_DIR, "media/pair_plot_1.png"))
    plt.show()

    sns.pairplot(df[['T1_BrainAge', 'PAD_GROUPS', 'Education', 'StrongProfile']])
    plt.savefig(os.path.join(BASE_DIR, "media/pair_plot_2.png"))
    plt.show()

    sns.pairplot(df[['T1_BrainAge', 'T1_ALSFRS', 'disease_duration_after_TP1', 'total_disease_duration']])
    plt.savefig(os.path.join(BASE_DIR, "media/pair_plot_3.png"))
    plt.show()

    # Create histogram
    plt.hist(df[['T1_BrainAge', 'T1_chronAge']])
    plt.savefig(os.path.join(BASE_DIR, "media/hist_plot.png"))
    plt.show()

    with open(os.path.join(BASE_DIR, 'media/ba_rf_model'), 'rb') as f:
        rf = pickle.load(f)

    X = df[['T1_chronAge', 'T1_PAD', 'Age_at_onset', 'premorbidIQ', 'PAD_GROUPS', 'Education', 'StrongProfile', 'T1_ALSFRS', 'disease_duration_after_TP1', 'total_disease_duration']]
    y = df['T1_BrainAge']
    y_pred = rf.predict(X)
    mse = mean_squared_error(y, y_pred)
    abr = mean_absolute_error(y, y_pred)

    context = {
        'mean_squared_error': abr,
        'accuracy': mse
    }

    print("Confusion Matrix:")
    print(abr)
    return render(request, "admin/adminml.html", context)
