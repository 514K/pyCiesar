def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','к')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','л')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','м')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','н')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','о')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','п')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','р')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','с')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','т')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','у')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','ф')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','х')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','ц')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','ч')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','ш')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','щ')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','ъ')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ы')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','ь')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','э')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ю')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','я')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','а')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','б')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','в')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','г')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','д')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','е')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','ё')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','ж')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','з')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','и')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','й')+a[k+1:]
    return a