import pandas as pd
import torch
from sklearn import model_selection


class RecipieDataset:
    def __init__(self,contributors,recipeId,averate_rating):
        self.contributors = contributors
        self.recipeId = recipeId
        self.averate_rating = averate_rating

    def __len__(self):
        return len(self.contributors)

    def __getitem__(self, item):
        contributors = self.contributors[item]
        recipeId = self.recipeId[item]
        averate_rating = self.averate_rating[item]

        return {"contributors": torch.tensor(contributors, dtype=torch.long),
                "recipeId": torch.tensor(recipeId, dtype=torch.long),
                "averate_rating": torch.tensor(averate_rating, dtype=torch.float),


        }

class RecSysModel():


    def train():
        df = pd.read_csv("set/recipeDF.csv")
        df_train, df_valid = model_selection.train_test_split(
            df, test_size=0.1, random_state=42, stratify=df.average_rating.values
        )

        train_dataset = RecipieDataset(
            contributors = df_train.contributors.value, recipeId = df_train.recipeId.value,averate_rating = df_train.averate_rating.value
        )
        valid_dataset = RecipieDataset(
            contributors = df_train.contributors.value, recipeId = df_train.recipeId.value,averate_rating = df_train.averate_rating.value
        )

if __name__ == "__main__":
    RecSysModel.train()