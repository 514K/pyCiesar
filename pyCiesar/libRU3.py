def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','г')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','д')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','е')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ё')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','ж')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','з')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','и')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','й')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','к')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','л')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','м')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','н')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','о')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','п')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','р')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','с')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','т')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','у')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','ф')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','х')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ц')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ч')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ш')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','щ')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','ъ')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','ы')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','ь')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','э')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','ю')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','я')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','а')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','б')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','в')+a[k+1:]
    return a