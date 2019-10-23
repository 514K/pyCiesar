def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','й')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','к')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','л')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','м')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','н')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','о')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','п')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','р')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','с')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','т')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','у')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','ф')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','х')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','ц')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','ч')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','ш')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','щ')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ъ')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','ы')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','ь')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','э')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ю')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','я')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','а')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','б')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','в')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','г')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','д')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','е')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','ё')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ж')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','з')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','и')+a[k+1:]
    return a