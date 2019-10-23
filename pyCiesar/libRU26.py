def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','щ')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','ъ')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','ы')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ь')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','э')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ю')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','я')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','а')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','б')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','в')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','г')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','д')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','е')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','ё')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','ж')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','з')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','и')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','й')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','к')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','л')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','м')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','н')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','о')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','п')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','р')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','с')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','т')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','у')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','ф')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','х')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ц')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','ч')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','ш')+a[k+1:]
    return a