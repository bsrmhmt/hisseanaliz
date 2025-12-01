# backend/indicators.py
import pandas as pd
import numpy as np

class TechnicalEngine:
    """Teknik analiz göstergelerini hesaplayan motor"""
    
    def add_all_indicators(self, df):
        df = df.copy()
        
        # 1. RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # 2. Hareketli Ortalamalar
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['SMA_200'] = df['Close'].rolling(window=200).mean()
        
        # 3. Bollinger Bantları
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['Std'] = df['Close'].rolling(window=20).std()
        df['BB_Upper'] = df['SMA_20'] + (df['Std'] * 2)
        df['BB_Lower'] = df['SMA_20'] - (df['Std'] * 2)
        
        # 4. Temizlik
        df.dropna(inplace=True)
        return df
