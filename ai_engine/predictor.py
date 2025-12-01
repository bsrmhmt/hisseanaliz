# ai_engine/predictor.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd

class AIPredictor:
    """Gelecek fiyat hareketlerini tahmin eden yapay zeka modeli"""
    
    def __init__(self):
        # 100 Karar ağacından oluşan bir orman kuruyoruz
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def predict(self, df, horizon=5):
        """
        Verilen veri setine göre T+horizon gün sonrasını tahmin eder.
        horizon: Kaç gün sonrasını tahmin edeceği (Varsayılan 5 gün)
        """
        try:
            data = df.copy()
            
            # Hedef: Gelecekteki Kapanış Fiyatı (Target)
            data['Target'] = data['Close'].shift(-horizon)
            
            # Makinenin kullanacağı özellikler (Features)
            features = ['RSI', 'SMA_50', 'SMA_200', 'BB_Upper', 'BB_Lower', 'Volume']
            
            # Sadece hesaplanmış (dolu) özellikleri seç
            valid_features = [f for f in features if f in data.columns]
            
            if not valid_features:
                return None, 0
                
            # Eğitim verisini hazırla (NaN olan son satırları at)
            data_clean = data.dropna(subset=['Target'] + valid_features)
            
            X = data_clean[valid_features]
            y = data_clean['Target']
            
            # Modeli Eğit (Fit)
            self.model.fit(X, y)
            
            # Tahmin Yap (Bugünün verisiyle geleceği gör)
            current_data = data.iloc[[-1]][valid_features] # Son gün
            prediction = self.model.predict(current_data)[0]
            
            # Güven Skoru (Hata Payı - MAE)
            # Geçmişte ne kadar yanıldığını test et
            history_preds = self.model.predict(X)
            mae = mean_absolute_error(y, history_preds)
            
            return prediction, mae
            
        except Exception as e:
            print(f"AI Hatası: {e}")
            return None, 0
