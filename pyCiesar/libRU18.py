def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','с')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','т')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','у')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ф')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','х')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ц')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','ч')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ш')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','щ')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ъ')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','ы')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','ь')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','э')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','ю')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','я')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','а')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','б')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','в')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','г')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','д')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','е')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ё')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ж')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','з')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','и')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','й')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','к')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','л')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','м')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','н')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','о')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','п')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','р')+a[k+1:]
    return a