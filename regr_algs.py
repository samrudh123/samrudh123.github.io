import numpy as np

class LinearRegression():
    def __init__(self, learning_rate=1e-4, tolerance=1e-8, iterations=10000):
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        self.iterations = iterations
        
    def fit(self, x, y):
        if len(x) != len(y):
            raise ValueError("No of input data does not match the output data") 
        if len(x)>1000:
            x = x[:1000]
            y = y[:1000]
        count = 0
        self.n_samples, self.n_features = x.shape
        self.b = 0
        self.w = np.zeros(self.n_features)
        db = 0
        dw = np.zeros(self.n_features)
        prev_db = 0
        prev_dw = np.zeros(self.n_features)
        for i in range(self.iterations):
            y_pred = self.predict(x)
            db =  2*np.sum(y_pred - y)/self.n_samples
            for j in range(self.n_features):
                dw[j] = 2*np.dot(x[:,j].T, (y_pred - y))/self.n_samples
            self.b = self.b - self.learning_rate*db
            self.w = self.w - self.learning_rate*dw
            
            abs_db_red = np.abs(db - prev_db)
            abs_dw_red = np.abs(dw - prev_dw)
            
            if abs_db_red < self.tolerance:
                for k in range(self.n_features):
                    if abs_dw_red[k] < self.tolerance:
                        count += 1
                if count == self.n_features:
                    break
                
            prev_db = db
            prev_dw = dw
        
    def predict(self, x):
        return np.dot(x, self.w) + self.b
    
class LassoRegression():
    def __init__(self, learning_rate=1e-4, tolerance=1e-8, iterations=10000, l1_penalty=10):
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        self.iterations = iterations
        self.l1_penalty = l1_penalty
        
    def fit(self, x, y):
        if len(x) != len(y):
            raise ValueError("No of input data does not match the output data") 
        if len(x)>1000:
            x = x[:1000]
            y = y[:1000]
        count = 0
        self.n_samples, self.n_features = x.shape
        self.b = 0
        self.w = np.zeros(self.n_features)
        db = 0
        dw = np.zeros(self.n_features)
        prev_db = 0
        prev_dw = np.zeros(self.n_features)
        for i in range(self.iterations):
            y_pred = self.predict(x)
            db =  2*np.sum(y_pred - y)/self.n_samples
            for j in range(self.n_features):
                if self.w[j] > 0:
                    dw[j] = (2*np.dot(x[:,j].T, (y_pred - y)) + self.l1_penalty)/self.n_samples
                else:
                    dw[j] = (2*np.dot(x[:,j].T, (y_pred - y)) - self.l1_penalty)/self.n_samples
            self.b = self.b - self.learning_rate*db
            self.w = self.w - self.learning_rate*dw
            
            abs_db_red = np.abs(db - prev_db)
            abs_dw_red = np.abs(dw - prev_dw)
            
            if abs_db_red < self.tolerance:
                for k in range(self.n_features):
                    if abs_dw_red[k] < self.tolerance:
                        count += 1
                if count == self.n_features:
                    break
                
            prev_db = db
            prev_dw = dw
        
    def predict(self, x):
        return np.dot(x, self.w) + self.b
    
class RidgeRegression():
    def __init__(self, learning_rate=1e-4, tolerance=1e-8, iterations=10000, l2_penalty=10):
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        self.iterations = iterations
        self.l2_penalty = l2_penalty
        
    def fit(self, x, y):
        if len(x) != len(y):
            raise ValueError("No of input data does not match the output data") 
        if len(x)>1000:
            x = x[:1000]
            y = y[:1000]
        count = 0
        self.n_samples, self.n_features = x.shape
        self.b = 0
        self.w = np.zeros(self.n_features)
        db = 0
        dw = np.zeros(self.n_features)
        prev_db = 0
        prev_dw = np.zeros(self.n_features)
        for i in range(self.iterations):
            y_pred = self.predict(x)
            db =  2*np.sum(y_pred - y)/self.n_samples
            for j in range(self.n_features):
                if self.w[j]>0:
                    dw[j] = (2*np.dot(x[:,j].T, (y_pred - y)) + 2*self.l2_penalty*self.w[j])/self.n_samples
            self.b = self.b - self.learning_rate*db
            self.w = self.w - self.learning_rate*dw
            
            abs_db_red = np.abs(db - prev_db)
            abs_dw_red = np.abs(dw - prev_dw)
            
            if abs_db_red < self.tolerance:
                for k in range(self.n_features):
                    if abs_dw_red[k] < self.tolerance:
                        count += 1
                if count == self.n_features:
                    break
                
            prev_db = db
            prev_dw = dw
        
    def predict(self, x):
        return np.dot(x, self.w) + self.b
    
class ElasticNet():
    def __init__(self, learning_rate=1e-4, tolerance=1e-8, iterations=10000, l1_penalty = 10, l2_penalty=10, l1_ratio=0.5):
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        self.iterations = iterations
        self.l1_penalty = l1_penalty
        self.l2_penalty = l2_penalty
        self.l1_ratio = l1_ratio
        
    def fit(self, x, y):
        if len(x) != len(y):
            raise ValueError("No of input data does not match the output data") 
        if len(x)>1000:
            x = x[:1000]
            y = y[:1000]
        count = 0
        self.n_samples, self.n_features = x.shape
        self.b = 0
        self.w = np.zeros(self.n_features)
        db = 0
        dw = np.zeros(self.n_features)
        prev_db = 0
        prev_dw = np.zeros(self.n_features)
        for i in range(self.iterations):
            y_pred = self.predict(x)
            db =  2*np.sum(y_pred - y)/self.n_samples
            for j in range(self.n_features):
                if self.w[j]>0:
                    dw[j] = (2*np.dot(x[:,j].T, (y_pred - y)) + self.l1_ratio*self.l1_penalty + (1-self.l1_ratio)*self.l2_penalty*self.w[j])/self.n_samples
                else:
                    dw[j] = (2*np.dot(x[:,j].T, (y_pred - y)) - self.l1_ratio*self.l1_penalty + (1-self.l1_ratio)*self.l2_penalty*self.w[j])/self.n_samples
            self.b = self.b - self.learning_rate*db
            self.w = self.w - self.learning_rate*dw
            
            abs_db_red = np.abs(db - prev_db)
            abs_dw_red = np.abs(dw - prev_dw)
            
            if abs_db_red < self.tolerance:
                for k in range(self.n_features):
                    if abs_dw_red[k] < self.tolerance:
                        count += 1
                if count == self.n_features:
                    break
                
            prev_db = db
            prev_dw = dw
        
    def predict(self, x):
        return np.dot(x, self.w) + self.b