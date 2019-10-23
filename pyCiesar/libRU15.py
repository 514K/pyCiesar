def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','о')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','п')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','р')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','с')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','т')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','у')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','ф')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','х')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ц')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ч')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','ш')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','щ')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','ъ')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','ы')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','ь')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','э')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','ю')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','я')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','а')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','б')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','в')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','г')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','д')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','е')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','ё')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','ж')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','з')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','и')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','й')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','к')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','л')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','м')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','н')+a[k+1:]
    return a