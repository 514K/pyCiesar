def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','у')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','ф')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','х')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ц')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','ч')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ш')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','щ')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ъ')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ы')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ь')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','э')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','ю')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','я')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','а')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','б')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','в')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','г')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','д')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','е')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','ё')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ж')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','з')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','и')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','й')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','к')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','л')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','м')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','н')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','о')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','п')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','р')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','с')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','т')+a[k+1:]
    return a