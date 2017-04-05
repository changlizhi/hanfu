'''
Created on 2016年6月10日

@author: me
'''

def ti_huan(tihuan_zhi):
    fuhao_chuan = "\040$\\\':\040$\\t:\040$\\n\', \':$&nbsp;:·$&middot;:?$&iexcl;:￠$&cent;:￡$&pound;:¤$&curren;:￥$&yen;:|$&brvbar;:§$&sect;:¨$&uml;:©$&copy;:a$&ordf;:?$&laquo;:?$&not;:/x7f$&shy;:®$&reg;:ˉ$&macr;:°$&deg;:±$&plusmn;:2$&sup2;:3$&sup3;:′$&acute;:μ$&micro;:?$&para;:·$&middot;:?$&cedil;:1$&sup1;:o$&ordm;:?$&raquo;:?$&frac14;:?$&frac12;:?$&frac34;:?$&iquest;:À$&Agrave;:\"$&quot;:&$&amp;:<$&lt;:>$&gt;:\' {$\" {:} \'$} \""
    fuhao_list = fuhao_chuan.split(":")
    for fuhao in fuhao_list:
        fuhao_chaifen = fuhao.split("$")
        tihuan_zhi = tihuan_zhi.replace(fuhao_chaifen[1],fuhao_chaifen[0])
    return tihuan_zhi
if __name__ == '__main__':
    print(ti_huan("\\nfewf"))