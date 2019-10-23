def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','э')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','ю')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','я')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','а')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','б')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','в')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','г')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','д')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','е')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','ё')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','ж')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','з')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','и')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','й')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','к')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','л')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','м')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','н')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','о')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','п')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','р')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','с')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','т')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','у')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','ф')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','х')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','ц')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','ч')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','ш')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','щ')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ъ')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','ы')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','ь')+a[k+1:]
    return a