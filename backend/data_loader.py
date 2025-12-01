# backend/data_loader.py
import yfinance as yf
import pandas as pd

class DataLoader:
    """Veri çekme işlemlerinden sorumlu sınıf"""
    
    def __init__(self):
        self.period = "2y" # Varsayılan veri geçmişi

    def get_data(self, symbol):
        """
        Ham hisse verisini ve temel bilgileri çeker.
        """
        try:
            ticker = yf.Ticker(symbol)
            # Geçmiş verisi
            history = ticker.history(period=self.period)
            
            # Temel bilgiler (Bilanço vb.)
            info = ticker.info
            
            if len(history) < 50:
                return None, None
                
            return history, info
        except Exception as e:
            print(f"Hata: {e}")
            return None, None
