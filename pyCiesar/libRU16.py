def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','п')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','р')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','с')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','т')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','у')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ф')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','х')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ц')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ч')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ш')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','щ')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','ъ')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','ы')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','ь')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','э')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','ю')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','я')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','а')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','б')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','в')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','г')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','д')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','е')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','ё')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','ж')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','з')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','и')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','й')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','к')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','л')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','м')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','н')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','о')+a[k+1:]
    return a