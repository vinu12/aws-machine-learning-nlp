import json 

from typing import Dict, Any 

class BagOfWords:
    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize the component.
        """
        self.name = 'BagOfWords'
        self.iife_script = '''<script>var BagOfWords=function(){"use strict";var pt=document.createElement("style");pt.textContent=`input.svelte-5idota{width:300px;overflow:scroll;height:38px}.description.svelte-5idota{font-size:16px;opacity:.9}#title-div.svelte-5idota{display:flex;align-items:center}section.svelte-5idota{margin:auto;padding-bottom:15px}table.svelte-5idota{font-size:16px;background-color:#fff;border-collapse:collapse}.table-head.svelte-5idota{padding:16px;font-size:16px;text-align:left;border:none}td.svelte-5idota{padding:16px;background-color:#fff;border-bottom:1px solid black;font-size:18px;text-align:center}button.svelte-5idota{padding:6px 10px;font-size:16px;border:1px solid black;text-align:center;margin:2px 8px;font-weight:700}button.svelte-5idota:hover,.active.svelte-5idota{color:#fff;background-color:coral}thead.svelte-5idota{border-bottom:1px solid black}
`,document.head.appendChild(pt);function Q(){}function gt(t){return t()}function vt(){return Object.create(null)}function R(t){t.forEach(gt)}function bt(t){return typeof t=="function"}function It(t,e){return t!=t?e==e:t!==e||t&&typeof t=="object"||typeof t=="function"}function Pt(t){return Object.keys(t).length===0}function s(t,e){t.appendChild(e)}function U(t,e,n){t.insertBefore(e,n||null)}function M(t){t.parentNode&&t.parentNode.removeChild(t)}function Z(t,e){for(let n=0;n<t.length;n+=1)t[n]&&t[n].d(e)}function r(t){return document.createElement(t)}function B(t){return document.createTextNode(t)}function m(){return B(" ")}function V(t,e,n,i){return t.addEventListener(e,n,i),()=>t.removeEventListener(e,n,i)}function h(t,e,n){n==null?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}function qt(t){return Array.from(t.childNodes)}function tt(t,e){e=""+e,t.wholeText!==e&&(t.data=e)}function D(t,e){t.value=e==null?"":e}function et(t,e,n){t.classList[n?"add":"remove"](e)}let ut;function X(t){ut=t}const Y=[],mt=[],nt=[],kt=[],Ft=Promise.resolve();let ft=!1;function Gt(){ft||(ft=!0,Ft.then(yt))}function dt(t){nt.push(t)}const ht=new Set;let lt=0;function yt(){const t=ut;do{for(;lt<Y.length;){const e=Y[lt];lt++,X(e),Ht(e.$$)}for(X(null),Y.length=0,lt=0;mt.length;)mt.pop()();for(let e=0;e<nt.length;e+=1){const n=nt[e];ht.has(n)||(ht.add(n),n())}nt.length=0}while(Y.length);for(;kt.length;)kt.pop()();ft=!1,ht.clear(),X(t)}function Ht(t){if(t.fragment!==null){t.update(),R(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(dt)}}const Jt=new Set;function Kt(t,e){t&&t.i&&(Jt.delete(t),t.i(e))}function Qt(t,e,n,i){const{fragment:c,after_update:u}=t.$$;c&&c.m(e,n),i||dt(()=>{const y=t.$$.on_mount.map(gt).filter(bt);t.$$.on_destroy?t.$$.on_destroy.push(...y):R(y),t.$$.on_mount=[]}),u.forEach(dt)}function Rt(t,e){const n=t.$$;n.fragment!==null&&(R(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}function Ut(t,e){t.$$.dirty[0]===-1&&(Y.push(t),Gt(),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function Vt(t,e,n,i,c,u,y,L=[-1]){const d=ut;X(t);const a=t.$$={fragment:null,ctx:[],props:u,update:Q,not_equal:c,bound:vt(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(e.context||(d?d.$$.context:[])),callbacks:vt(),dirty:L,skip_bound:!1,root:e.target||d.$$.root};y&&y(a.root);let x=!1;if(a.ctx=n?n(t,e.props||{},(f,$,...k)=>{const W=k.length?k[0]:$;return a.ctx&&c(a.ctx[f],a.ctx[f]=W)&&(!a.skip_bound&&a.bound[f]&&a.bound[f](W),x&&Ut(t,f)),$}):[],a.update(),x=!0,R(a.before_update),a.fragment=i?i(a.ctx):!1,e.target){if(e.hydrate){const f=qt(e.target);a.fragment&&a.fragment.l(f),f.forEach(M)}else a.fragment&&a.fragment.c();e.intro&&Kt(t.$$.fragment),Qt(t,e.target,e.anchor,e.customElement),yt()}X(d)}class Xt{$destroy(){Rt(this,1),this.$destroy=Q}$on(e,n){if(!bt(n))return Q;const i=this.$$.callbacks[e]||(this.$$.callbacks[e]=[]);return i.push(n),()=>{const c=i.indexOf(n);c!==-1&&i.splice(c,1)}}$set(e){this.$$set&&!Pt(e)&&(this.$$.skip_bound=!0,this.$$set(e),this.$$.skip_bound=!1)}}const ee="";function xt(t,e,n){const i=t.slice();return i[15]=e[n],i}function wt(t,e,n){const i=t.slice();return i[15]=e[n],i}function Ct(t,e,n){const i=t.slice();return i[15]=e[n],i}function $t(t,e,n){const i=t.slice();return i[15]=e[n],i}function Et(t){let e,n=t[15]+"",i;return{c(){e=r("th"),i=B(n),h(e,"class","table-head svelte-5idota")},m(c,u){U(c,e,u),s(e,i)},p(c,u){u&16&&n!==(n=c[15]+"")&&tt(i,n)},d(c){c&&M(e)}}}function St(t){let e,n=t[7][t[15]]+"",i;return{c(){e=r("td"),i=B(n),h(e,"class","svelte-5idota")},m(c,u){U(c,e,u),s(e,i)},p(c,u){u&144&&n!==(n=c[7][c[15]]+"")&&tt(i,n)},d(c){c&&M(e)}}}function Bt(t){let e,n=t[6][t[15]]+"",i;return{c(){e=r("td"),i=B(n),h(e,"class","svelte-5idota")},m(c,u){U(c,e,u),s(e,i)},p(c,u){u&80&&n!==(n=c[6][c[15]]+"")&&tt(i,n)},d(c){c&&M(e)}}}function Ot(t){let e,n=t[5][t[15]]+"",i;return{c(){e=r("td"),i=B(n),h(e,"class","svelte-5idota")},m(c,u){U(c,e,u),s(e,i)},p(c,u){u&48&&n!==(n=c[5][c[15]]+"")&&tt(i,n)},d(c){c&&M(e)}}}function Yt(t){let e,n,i,c,u,y,L,d,a,x,f,$,k,W,O,I,z,P,ot,it,w,E,S,A,zt,j,At,Lt,q,ct,st,Wt,N,jt,Nt,F,rt,at,Tt,T,Mt,_t,Dt,G=t[4],p=[];for(let o=0;o<G.length;o+=1)p[o]=Et($t(t,G,o));let H=t[4],g=[];for(let o=0;o<H.length;o+=1)g[o]=St(Ct(t,H,o));let J=t[4],v=[];for(let o=0;o<J.length;o+=1)v[o]=Bt(wt(t,J,o));let K=t[4],b=[];for(let o=0;o<K.length;o+=1)b[o]=Ot(xt(t,K,o));return{c(){e=r("section"),n=r("h2"),n.textContent="Bag of Words Demo",i=m(),c=r("p"),c.textContent=`Edit the sentences and watch the corresponding vocabulary and cell-counts
    update:`,u=m(),y=r("br"),L=m(),d=r("div"),a=r("p"),a.textContent="Count Method:",x=m(),f=r("button"),f.textContent="Count",$=m(),k=r("button"),k.textContent="Binary",W=m(),O=r("table"),I=r("thead"),z=r("tr"),P=r("th"),ot=m();for(let o=0;o<p.length;o+=1)p[o].c();it=m(),w=r("tbody"),E=r("tr"),S=r("td"),A=r("div"),zt=B(`Sentence 1:
            `),j=r("input"),At=m();for(let o=0;o<g.length;o+=1)g[o].c();Lt=m(),q=r("tr"),ct=r("td"),st=r("div"),Wt=B(`Sentence 2:
            `),N=r("input"),jt=m();for(let o=0;o<v.length;o+=1)v[o].c();Nt=m(),F=r("tr"),rt=r("td"),at=r("div"),Tt=B(`Sentence 3:
            `),T=r("input"),Mt=m();for(let o=0;o<b.length;o+=1)b[o].c();h(c,"class","description svelte-5idota"),h(a,"class","description svelte-5idota"),h(f,"class","svelte-5idota"),et(f,"active",t[3]==="count"),h(k,"class","svelte-5idota"),et(k,"active",t[3]==="ohe"),h(d,"id","title-div"),h(d,"class","svelte-5idota"),h(I,"class","svelte-5idota"),h(j,"class","svelte-5idota"),h(S,"class","table-head svelte-5idota"),h(N,"class","svelte-5idota"),h(ct,"class","table-head svelte-5idota"),h(T,"class","svelte-5idota"),h(rt,"class","table-head svelte-5idota"),h(O,"class","svelte-5idota"),h(e,"class","svelte-5idota")},m(o,_){U(o,e,_),s(e,n),s(e,i),s(e,c),s(e,u),s(e,y),s(e,L),s(e,d),s(d,a),s(d,x),s(d,f),s(d,$),s(d,k),s(e,W),s(e,O),s(O,I),s(I,z),s(z,P),s(z,ot);for(let l=0;l<p.length;l+=1)p[l].m(z,null);s(O,it),s(O,w),s(w,E),s(E,S),s(S,A),s(A,zt),s(A,j),D(j,t[0]),s(E,At);for(let l=0;l<g.length;l+=1)g[l].m(E,null);s(w,Lt),s(w,q),s(q,ct),s(ct,st),s(st,Wt),s(st,N),D(N,t[1]),s(q,jt);for(let l=0;l<v.length;l+=1)v[l].m(q,null);s(w,Nt),s(w,F),s(F,rt),s(rt,at),s(at,Tt),s(at,T),D(T,t[2]),s(F,Mt);for(let l=0;l<b.length;l+=1)b[l].m(F,null);_t||(Dt=[V(f,"click",t[9]),V(k,"click",t[10]),V(j,"input",t[11]),V(N,"input",t[12]),V(T,"input",t[13])],_t=!0)},p(o,[_]){if(_&8&&et(f,"active",o[3]==="count"),_&8&&et(k,"active",o[3]==="ohe"),_&16){G=o[4];let l;for(l=0;l<G.length;l+=1){const C=$t(o,G,l);p[l]?p[l].p(C,_):(p[l]=Et(C),p[l].c(),p[l].m(z,null))}for(;l<p.length;l+=1)p[l].d(1);p.length=G.length}if(_&1&&j.value!==o[0]&&D(j,o[0]),_&144){H=o[4];let l;for(l=0;l<H.length;l+=1){const C=Ct(o,H,l);g[l]?g[l].p(C,_):(g[l]=St(C),g[l].c(),g[l].m(E,null))}for(;l<g.length;l+=1)g[l].d(1);g.length=H.length}if(_&2&&N.value!==o[1]&&D(N,o[1]),_&80){J=o[4];let l;for(l=0;l<J.length;l+=1){const C=wt(o,J,l);v[l]?v[l].p(C,_):(v[l]=Bt(C),v[l].c(),v[l].m(q,null))}for(;l<v.length;l+=1)v[l].d(1);v.length=J.length}if(_&4&&T.value!==o[2]&&D(T,o[2]),_&48){K=o[4];let l;for(l=0;l<K.length;l+=1){const C=xt(o,K,l);b[l]?b[l].p(C,_):(b[l]=Ot(C),b[l].c(),b[l].m(F,null))}for(;l<b.length;l+=1)b[l].d(1);b.length=K.length}},i:Q,o:Q,d(o){o&&M(e),Z(p,o),Z(g,o),Z(v,o),Z(b,o),_t=!1,R(Dt)}}}function Zt(t,e,n){let i,c,u,y,L,d="I",a="love dogs",x="dogs dogs dogs",f="count";function $(P,ot,it){let w={},E=ot.replace(/[^\w\s]/gi,"").toLowerCase();for(const S of P)it==="count"?w[S]=E.split(" ").filter(A=>A===S).length:w[S]=E.split(" ").filter(A=>A===S).length?1:0;return w}const k=()=>{n(3,f="count")},W=()=>{n(3,f="ohe")};function O(){d=this.value,n(0,d)}function I(){a=this.value,n(1,a)}function z(){x=this.value,n(2,x)}return t.$$.update=()=>{t.$$.dirty&7&&n(8,i=(d+" "+a+" "+x).replace(/[^\w\s]/gi,"").toLowerCase()),t.$$.dirty&256&&console.log("tokens",i),t.$$.dirty&256&&n(4,c=Array.from(new Set(i.split(" "))).filter(P=>P!=="")),t.$$.dirty&16&&console.log("vocab",c),t.$$.dirty&25&&n(7,u=$(c,d,f)),t.$$.dirty&26&&n(6,y=$(c,a,f)),t.$$.dirty&28&&n(5,L=$(c,x,f))},[d,a,x,f,c,L,y,u,i,k,W,O,I,z]}class te extends Xt{constructor(e){super(),Vt(this,e,Zt,Yt,It,{})}}return te}();
</script>'''
        self.div_id = 'BagOfWords-328cd234'
        self.props = []
        self.markup = ""
        self.add_params(kwargs)

    def add_params(self, params: Dict[str, Any]) -> None:
        """
        Add parameters to the component and serve in html.

        Parameters
        ----------
        params : dict
            The parameters to add to the component.
        """
        js_data = json.dumps(params, indent=0)
        self.markup = f"""
        <div id="{self.div_id}"></div>
        <script>
        (() => {{
            var data = {js_data};
            window.{self.name}_data = data;
            var {self.name}_inst = new {self.name}({{
                "target": document.getElementById("{self.div_id}"),
                "props": data
            }});
        }})();
        </script>
        """

    def _repr_html_(self) -> str:
        """
        Return the component as an HTML string.
        """
        return f"""
        {self.iife_script}
        {self.markup}
        """

    def __call__(self, **kwargs: Any) -> "BagOfWords":
        """
        Call the component with the given kwargs.

        Parameters
        ----------
        kwargs : any
            The kwargs to pass to the component.

        Returns
        -------
        PackagedComponent
            A python class representing the svelte component, renderable in Jupyter.
        """
        # render with given arguments
        self.add_params(kwargs)
        return self
