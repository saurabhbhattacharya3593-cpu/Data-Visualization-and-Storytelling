"""Reproduce basic analysis. Dataset is synthetic practice data."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data.csv",parse_dates=["Order_Date"])
print("Shape:",df.shape,"\\nMissing values:\\n",df.isna().sum())
print("Duplicate order IDs:",df.Order_ID.duplicated().sum())
sales=df.Sales.sum(); profit=df.Profit.sum()
print(f"Sales: ${sales:,.2f} | Profit: ${profit:,.2f} | Margin: {profit/sales:.1%}")
monthly=df.set_index("Order_Date").resample("MS")[["Sales","Profit"]].sum()
monthly.Sales.plot(figsize=(10,5),marker="o",title="Monthly Sales Trend")
plt.ylabel("Sales (USD)"); plt.grid(alpha=.25); plt.tight_layout(); plt.show()
print(df.groupby("Category")[["Sales","Profit"]].sum().sort_values("Sales",ascending=False))
