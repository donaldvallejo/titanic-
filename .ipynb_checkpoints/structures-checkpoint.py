# Importations and Initializations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def display_survivability():
  figure = plt.figure(figsize=(18, 7))
  grids = figure.add_gridspec(1, 2)
  grids.update(wspace=0.3, hspace=0.15)
  ax0 = figure.add_subplot(grids[0, 0])
  ax1 = figure.add_subplot(grids[0, 1])

  TITLE_AX0 = "[ TARGET VALUE ]\n___________\n\nSURVIVED RATE"
  ax0.text(0.5, 0.5, 
          TITLE_AX0,
          horizontalalignment="center",
          verticalalignment="center",
          fontsize=28,
          fontweight="bold",
          fontfamily="serif",
          color="#000000")

  ax0.set_xticklabels([]); ax0.set_yticklabels([])
  ax0.tick_params(left=False, bottom=False)

  ax_survived = ax1
  sns.countplot(x="Survived",
                color="gray",
                data=df_utility,
                ax=ax_survived,
                palette="gist_gray")
  sns.despine()

  ax0.spines["top"].set_visible(False)
  ax0.spines["left"].set_visible(False)
  ax0.spines["bottom"].set_visible(False)
  ax0.spines["right"].set_visible(False)

  plt.show();

def display_categorical_distributions(title="Categorical Features", track_survivability=False):
  figure = plt.figure(figsize=(18, 15))
  grids = figure.add_gridspec(3, 3)
  palette = "gist_gray"

  ax0 = figure.add_subplot(grids[0, 0])
  ax1 = figure.add_subplot(grids[0, 1])
  ax2 = figure.add_subplot(grids[0, 2])
  ax3 = figure.add_subplot(grids[1, 0])
  ax4 = figure.add_subplot(grids[1, 1])

  if track_survivability is True:
    hue = "Survived"
  else:
    hue = None

  ax_sex = ax0
  sns.countplot(x="Sex", hue=hue, data=df_utility, ax=ax_sex, palette=palette)
  sns.despine()

  ax_parch = ax1
  sns.countplot(x="Parch", hue=hue, data=df_utility, ax=ax_parch, palette=palette)
  sns.despine()

  ax_embarked = ax2
  sns.countplot(x="Embarked", hue=hue, data=df_utility, ax=ax_embarked, palette=palette)
  sns.despine()

  ax_pclass = ax3
  sns.countplot(x="Pclass", hue=hue, data=df_utility, ax=ax_pclass, palette=palette)
  sns.despine()

  ax_sibsip = ax4
  sns.countplot(x="SibSp", hue=hue, data=df_utility, ax=ax_sibsip, palette=palette)
  sns.despine()

  figure.suptitle(title, fontweight="bold", fontsize=20)
  figure.text(s="Sex, Parch, Embarked, Pclass, SibSip", 
          x=0.5, y=0.94, ha="center",va="top")

  plt.show();

def display_continuous_distributions(with_survivability=False):
  if with_survivability is True:
    figure = plt.figure(figsize=(18, 15))
    grids = figure.add_gridspec(3, 3)
    palette = "gist_gray_r"

    ax0 = figure.add_subplot(grids[0, 0])
    ax1 = figure.add_subplot(grids[0, 1])

    ax_sex = ax0
    sns.kdeplot(x="Age", hue="Survived", data=df_utility, fill=True, alpha=0.5, 
                shade=True, ax=ax_sex, palette=palette)
    sns.despine()

    ax_parch = ax1
    sns.kdeplot(x="Fare", hue="Survived", data=df_utility, fill=True, alpha=0.5, 
                shade=True, ax=ax_parch, palette=palette)
    sns.despine()

    figure.suptitle("Continous Features with Survivability", fontweight="bold", fontsize=20)
    figure.text(s="Age, Fare", x=0.5, y=0.94, ha="center", va="top", fontsize=15)
  else:
    figure = plt.figure(figsize=(15, 8))
    grids = figure.add_gridspec(2, 3)
    palette = "gist_gray"; palette_r = "gist_gray_r"

    ax0 = figure.add_subplot(grids[0, 0])
    ax1 = figure.add_subplot(grids[0, 1])
    ax2 = figure.add_subplot(grids[1, 0])
    ax3 = figure.add_subplot(grids[1, 1])

    ax_sex = ax0
    sns.kdeplot(x="Age", color="gray", shade=True, alpha=0.5, data=df_utility, ax=ax_sex, palette=palette)
    sns.despine()

    ax_sex2 = ax2
    sns.boxenplot(x="Age", hue="Survived", data=df_utility, ax=ax_sex2, palette=palette_r)
    sns.despine()

    ax_sex = ax1
    sns.kdeplot(x="Fare", color="gray", shade=True, alpha=0.5, data=df_utility, ax=ax_sex, palette=palette)
    sns.despine()

    ax_fare2 = ax3
    sns.boxenplot(x="Fare", hue="Survived", data=df_utility, ax=ax_fare2, palette=palette_r)
    sns.despine()

    title_spaced = "               Age                                   Fare"
    figure.text(0.1, 1, title_spaced, fontsize=20, fontweight="bold", fontfamily="serif", ha="left") 

  plt.show();

