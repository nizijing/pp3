from dataclasses import dataclass, field

@dataclass
class App:
    name: str = 'test'
    namespace: str = field(init=False)
    replicas: int = field(default = 1) 
    first_image_tag: str = field(init=False)

    def __post_init__(self):
        pass
        
    def update_replicas(self):
        self.replicas = 2 if self.namespace == 'production' else 1
