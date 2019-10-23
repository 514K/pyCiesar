def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','р')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','с')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','т')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','у')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','ф')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','х')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','ц')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ч')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ш')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','щ')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','ъ')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','ы')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','ь')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','э')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','ю')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','я')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','а')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','б')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','в')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','г')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','д')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','е')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ё')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','ж')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','з')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','и')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','й')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','к')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','л')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','м')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','н')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','о')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','п')+a[k+1:]
    return a