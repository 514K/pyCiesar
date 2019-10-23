def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','н')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','о')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','п')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','р')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','с')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','т')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','у')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ф')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','х')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ц')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','ч')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','ш')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','щ')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','ъ')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','ы')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','ь')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','э')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ю')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','я')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','а')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','б')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','в')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','г')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','д')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','е')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','ё')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','ж')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','з')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','и')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','й')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','к')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','л')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','м')+a[k+1:]
    return a