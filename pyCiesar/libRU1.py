def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','б')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','в')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','г')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','д')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','е')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ё')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','ж')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','з')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','и')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','й')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','к')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','л')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','м')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','н')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','о')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','п')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','р')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','с')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','т')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','у')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ф')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','х')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ц')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','ч')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','ш')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','щ')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','ъ')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','ы')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','ь')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','э')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ю')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','я')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','а')+a[k+1:]
    return a