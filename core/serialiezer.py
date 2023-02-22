from rest_framework import serializers
from .models import Bahan, Obat

def build_url(url):
    return f'http://127.0.0.1:8000{url}'

class BahanSerializer(serializers.ModelSerializer):
    
    gambar = serializers.SerializerMethodField()
    
    def get_gambar(self, obj):
        return build_url(obj.gambar)
    
    class Meta:
        model = Bahan
        fields = ('nama_bahan','gambar', 'keterangan')
        
class ObatSerializer(serializers.ModelSerializer):
    gambar = serializers.SerializerMethodField()
    # bahan_1 = BahanSerializer()
    # bahan_2 = BahanSerializer()
    # bahan_3 = BahanSerializer()
    # bahan_4 = BahanSerializer()
    # bahan_5 = BahanSerializer()
    # bahan_6 = BahanSerializer()
    # bahan_7 = BahanSerializer()

    bahan = serializers.SerializerMethodField()

    def get_bahan(self, obj):
        bahan = []
        bahan_1 = BahanSerializer(obj.bahan_1).data
        bahan_2 = BahanSerializer(obj.bahan_2).data
        bahan_3 = BahanSerializer(obj.bahan_3).data
        bahan_4 = BahanSerializer(obj.bahan_4).data
        bahan_5 = BahanSerializer(obj.bahan_5).data
        bahan_6 = BahanSerializer(obj.bahan_6).data
        bahan_7 = BahanSerializer(obj.bahan_7).data
        
        for i in [bahan_1, bahan_2, bahan_3, bahan_4, bahan_5, bahan_6, bahan_7]:
            if i['nama_bahan'] and i['gambar'] and i['keterangan'] == None:
                pass
            elif i['nama_bahan'] and i['gambar'] and i['keterangan'] != None:
                bahan.append(i)

        return bahan
            
        
    def get_gambar(self, obj):
        return build_url(obj.gambar)
    
    class Meta:
        model = Obat
        fields = (
            'id',
            'nama_obat',
            'keterangan',
            'gambar',
            'bahan'
            # 'bahan_1',
            # 'bahan_2',
            # 'bahan_3',
            # 'bahan_4',
            # 'bahan_5'
            )