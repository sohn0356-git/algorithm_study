#include <iostream>

using namespace std;

int N, P, A;
int ans;
int MOD = 1000000007;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin>> P >> N >> A;
    ans += A;
    for (int i=1;i<N;i++)
    {
        ans *= P;
        cin>>A;
        ans += A;
    }
    cout<<ans;
    return 0;
}